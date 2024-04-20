import { useEffect, useState } from "react";
import { TransitStop } from "./types/TransitStop";
import { TransitStopComponent } from "./components/TransitStopComponent";
import { StopsMapComponent } from "./components/StopsMapComponent";
import { StopsMap } from "./types/StopsMap";

const mapSettings: StopsMap = {
  zoom: 16,
  centerLat: 52.21858,
  centerLng: 21.013381991779095
}

const placeholderStops: TransitStop[] = [
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
  {
    departures: [
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
      {
        line: "4",
        direction: "Rondo Żaba",
        arrivalTime: new Date(Date.now()),
      },
    ],
    isBusStop: false,
    name: "Plac Politechniki 01",
    walkTime: 2,
  },
];

function App() {
  const [stops, setStops] = useState<TransitStop[]>([]);

  useEffect(() => {
    setStops(placeholderStops);
    // TODO: komunikacja z API
  }, []);

  return (
    <div className="w-full h-screen text-nowrap">
      <div className="h-[65%] grid grid-cols-3">
        {stops.map((item) => (
          <TransitStopComponent stop={item} />
        ))}
      </div>
      <div className="flex h-[35%] bg-slate-700 items-center justify-center">
        <StopsMapComponent mapSettings={mapSettings}/>
      </div>
    </div>
  );
}

export default App;
