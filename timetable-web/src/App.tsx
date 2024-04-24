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
      .then((data) => {
        setStops(data);
        console.log(data);
      })
      .catch((error) => console.error(error));
  }, []);

  return (
    <div className="w-full h-screen text-nowrap bg-[#3B3B4B]">
      <div className="flex h-[25%] items-center justify-center p-6">
        <StopsMapComponent mapStops={{ stops: stops }} />
      </div>
      <div className="h-[74%] grid grid-cols-3 gap-3 mx-4 ">
        {stops.map((item) => (
          <TransitStopComponent stop={item} />
        ))}
      </div>
    </div>
  );
}

export default App;
