'use client';

type AlgoExplanationProps = {
  algorithm: string;
  explanation: string;
};

export default function AlgoExplanation({ algorithm, explanation }: AlgoExplanationProps) {
  return (
    <div className="p-4 bg-gray-100 rounded-lg mb-6">
      <h2 className="text-xl font-bold mb-2">{algorithm} Explanation</h2>
      <div className="whitespace-pre-line">{explanation}</div>
    </div>
  );
}