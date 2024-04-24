import { useEffect, useState } from "react";
import { TransitStop } from "./types/TransitStop";
import { TransitStopComponent } from "./components/TransitStopComponent";
import { StopsMapComponent } from "./components/StopsMapComponent";
import { StopsMap } from "./types/StopsMap";
import stopsService from "./services/stops";


// const mapSettings: StopsMap = {
//   zoom: 16,
//   centerLat: 52.21858,
//   centerLng: 21.013381991779095
// }

function App() {
  const [stops, setStops] = useState<TransitStop[]>([]);

  useEffect(() => {
    stopsService
      .getAllStops()
      .then(data => {let slicedData = data.slice(0,6); setStops(slicedData); console.log(data)})
      .catch(error => console.error(error));    
  }, []);

  return (
    <div className="w-full h-screen text-nowrap">
      <div className="h-[65%] grid grid-cols-3">
        {stops.map((item) => (
          <TransitStopComponent stop={item} />
        ))}
      </div>
      <div className="flex h-[35%] bg-slate-700 items-center justify-center">
        <StopsMapComponent mapStops={{"stops": stops}}/>
      </div>
    </div>
  );
}

export default App;
