// Helper functions for algorithm visualization
export const generateRandomArray = (size: number = 10): number[] => {
    return Array.from({ length: size }, () => Math.floor(Math.random() * 100) + 5);
  };
  
  export const getBarColor = (
    index: number,
    currentStep: any
  ): string => {
    if (!currentStep) return 'bg-blue-500';
    
    if (index === currentStep.pivot) return 'bg-red-500';
    if (index >= currentStep.left && index <= currentStep.right) return 'bg-yellow-500';
    return 'bg-blue-500';
  };
  
  export const algorithmMetadata = {
    quicksort: {
      name: 'QuickSort',
      complexity: 'O(n log n) average, O(n²) worst case',
    },
    bubblesort: {
      name: 'Bubble Sort',
      complexity: 'O(n²)',
    },
  };