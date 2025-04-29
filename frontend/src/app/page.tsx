import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen p-8 font-sans">
      <main className="max-w-4xl mx-auto text-center">
        <h1 className="text-4xl font-bold mb-6">AlgoWise</h1>
        <p className="mb-8 text-lg">
          Visualize and understand fundamental computer science algorithms
        </p>
        
        <div className="grid md:grid-cols-2 gap-6 mb-8">
          <AlgorithmCard 
            title="Sorting Algorithms" 
            description="QuickSort, Bubble Sort, Merge Sort"
            href="/sort"
          />
          <AlgorithmCard 
            title="Graph Algorithms" 
            description="DFS, BFS, Dijkstra's"
            href="/graph"
          />
        </div>

        <Link 
          href="/sort" 
          className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 inline-block"
        >
          Start Learning
        </Link>
      </main>
    </div>
  );
}

const AlgorithmCard = ({ title, description, href }: { title: string, description: string, href: string }) => (
  <Link 
    href={href}
    className="p-6 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors text-left"
  >
    <h2 className="text-xl font-bold mb-2">{title}</h2>
    <p className="text-gray-600">{description}</p>
  </Link>
);