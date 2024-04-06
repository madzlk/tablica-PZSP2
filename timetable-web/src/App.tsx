
function App() {
  const stops = ["01", "02", "03", "04", "05", "06"]

  return (
    <div className="w-full h-screen">
      <div className="h-[67%] grid grid-cols-3 grid-rows-2">
        {stops.map((item) => <div className="p-2 text-xl border-2">Przystanek {item}</div>)}
      </div>
      <div className="flex h-[33%] bg-slate-700 items-center justify-center">
        <h2 className="text-white text-3xl">Tu może być mapa</h2>
      </div>
    </div>
  )
}

export default App
