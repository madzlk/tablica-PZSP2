import { useEffect, useState } from "react";
import { TransitStop } from "./types/TransitStop";
import { Departure } from "./types/Departure";
import { DepartureComponent } from "./components/DepartureComponent";

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
  }, []);

  return (
    <div className="w-full h-screen">
      <div className="h-[67%] grid grid-cols-3">
        {stops.map((item) => (
          <div className="flex flex-col p-2 text-xl border-2">
            <div className="mb-3 border-b-4">
              <h2>{item.name} </h2>
            </div>
            <span className="flex flex-col">
              {item.departures.map((departure) => (
                <DepartureComponent departure={departure} />
              ))}
            </span>
          </div>
        ))}
      </div>
      <div className="flex h-[33%] bg-slate-700 items-center justify-center">
        <h2 className="text-white text-3xl">Tu może być mapa</h2>
      </div>
    </div>
  );
}

export default App;
