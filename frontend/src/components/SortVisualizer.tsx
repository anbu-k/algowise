'use client';
import { useState, useEffect } from 'react';

export default function SortVisualizer() {
  const [originalArray] = useState([5, 3, 8, 4, 2]);
  const [currentArray, setCurrentArray] = useState([...originalArray]);
  const [steps, setSteps] = useState<any[]>([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isSorting, setIsSorting] = useState(false);
  const [explanation, setExplanation] = useState('');

  const runQuickSort = async () => {
    setIsSorting(true);
    const response = await fetch('http://localhost:8000/sort/quicksort', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(originalArray), // Sends raw array
    });
    const result = await response.json();
    setSteps(result.steps);
    setExplanation(result.explanation);
    setCurrentStep(0);
  };

  useEffect(() => {
    if (steps.length > 0 && currentStep < steps.length) {
      const timer = setTimeout(() => {
        setCurrentArray(steps[currentStep].array);
        setCurrentStep(currentStep + 1);
      }, 500); // Adjust speed here
      return () => clearTimeout(timer);
    } else {
      setIsSorting(false);
    }
  }, [currentStep, steps]);

  const reset = () => {
    setCurrentArray([...originalArray]);
    setSteps([]);
    setCurrentStep(0);
  };

  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">QuickSort Visualizer</h1>
      
      {/* Visualization */}
      <div className="flex items-end h-64 gap-1 mb-6 bg-gray-100 p-4 rounded">
        {currentArray.map((value, i) => {
          const isPivot = steps[currentStep - 1]?.pivot === i;
          const isComparing = steps[currentStep - 1]?.left <= i && i <= steps[currentStep - 1]?.right;
          
          return (
            <div
              key={i}
              className={`rounded-t-sm w-8 transition-all duration-300 ${
                isPivot ? 'bg-red-500' : 
                isComparing ? 'bg-yellow-500' : 'bg-blue-500'
              }`}
              style={{ height: `${value * 20}px` }}
            />
          );
        })}
      </div>

      {/* Controls */}
      <div className="flex gap-4 mb-6">
        <button
          onClick={runQuickSort}
          disabled={isSorting}
          className={`px-4 py-2 rounded text-white ${
            isSorting ? 'bg-gray-400' : 'bg-green-500 hover:bg-green-600'
          }`}
        >
          {isSorting ? 'Sorting...' : 'Run QuickSort'}
        </button>
        <button
          onClick={reset}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      {/* Explanation */}
      {explanation && (
        <div className="p-4 bg-gray-100 rounded mb-6">
          <h2 className="font-bold mb-2">How QuickSort Works:</h2>
          <p className="whitespace-pre-line">{explanation}</p>
        </div>
      )}

      {/* Step Counter */}
      {steps.length > 0 && (
        <div className="text-sm text-gray-600">
          Step {Math.min(currentStep, steps.length)} of {steps.length}
        </div>
      )}
    </div>
  );
}