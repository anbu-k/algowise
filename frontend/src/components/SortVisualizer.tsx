'use client'; 

import { useState } from 'react';

export default function SortVisualizer() {
  const [array, setArray] = useState([5, 3, 8, 4, 2]);
  const [sortedArray, setSortedArray] = useState<number[]>([]);

  const runQuickSort = async () => {
    const response = await fetch('/api/sort', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ array }),
    });
    const result = await response.json();
    setSortedArray(result.sorted);
  };

  return (
    <div>
      <div className="flex items-end h-64 gap-1 mb-4">
        {array.map((value, i) => (
          <div
            key={i}
            className="bg-blue-500 rounded-t-sm w-8"
            style={{ height: `${value * 20}px` }}
          />
        ))}
      </div>
      <button 
        onClick={runQuickSort}
        className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
      >
        Run QuickSort
      </button>
      {sortedArray.length > 0 && (
        <div className="mt-4 p-4 bg-gray-100 rounded">
          <p>Sorted Array: {JSON.stringify(sortedArray)}</p>
        </div>
      )}
    </div>
  );
}