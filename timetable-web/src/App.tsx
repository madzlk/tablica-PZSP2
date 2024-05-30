import { useEffect, useState } from "react";
import { TransitStop } from "./types/TransitStop";
import { TransitStopComponent } from "./components/TransitStopComponent";
import { StopsMapComponent } from "./components/StopsMapComponent";
import stopsService from "./services/stops";


function App() {
  const [stops, setStops] = useState<TransitStop[]>([]);

  // compare stops ids and return true if they are equal or false if they are not
  const areIdsEqual = (fetchedStops: TransitStop[], currentStops: TransitStop[]): boolean => {
    const fetchedIds = new Set(fetchedStops.map(stop => stop.id));
    const currentIds = new Set(currentStops.map(stop => stop.id));

    if (fetchedIds.size !== currentIds.size) return false;

    for(let id of fetchedIds) {
      if (!currentIds.has(id)) return false;
    }

    return true;
  };

  useEffect(() => {
    const fetchData = () => {
      stopsService
        .getAllStops()
        .then((data) => {
          if (!areIdsEqual(data, stops)) {
            data = stopsService.adjustDistances(data);
            setStops(data);
          } else {
            console.log('Stops are the same')
          }
        })
        .catch((error) => console.error(error));
    };

    fetchData();

    const interval = setInterval(() => {
      console.log("Fetching stops");
      fetchData();
    }, 60 * 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="w-full h-screen text-nowrap bg-[#3B3B4B] horizontal:flex horizontal:flex-row horizontal:justify-between">
      <div className="flex h-[25%] horizontal:h-full horizontal:w-[25%] items-center justify-center p-6">
        <StopsMapComponent mapStops={{ stops: stops }} />
      </div>
      <div
        className={`h-[74%] horizontal:h-full horizontal:w-[74%] grid grid-cols-${
          stops.length < 13 ? "2" : "3"
        } horizontal:grid-cols-4 horizontal:p-2 gap-3 mx-4`}
      >
        {stops.map(stop => (
          <TransitStopComponent
            key={stop.id}
            stop={stop}
            stops={stops}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
