import Link from 'next/link';

export default function Home() {
  return (
    <div className="grid min-h-screen p-8 font-sans">
      <main className="flex flex-col items-center gap-8">
        <h1 className="text-4xl font-bold">Algorithm Tutor</h1>
        <Link 
          href="/sort" 
          className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
        >
          Start Sorting Visualizer
        </Link>
      </main>
    </div>
  );
}