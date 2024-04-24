import { TransitStop } from "../types/TransitStop";
import { DepartureComponent } from "./DepartureComponent";
import { useEffect, useState } from "react";
import stops from "../services/stops";
import { Departure } from "../types/Departure";

interface Props {
  stop: TransitStop;
}

export const TransitStopComponent = ({ stop }: Props) => {
  const [departures, setDepartures] = useState<Departure[]>([]);

  useEffect(() => {
    const fetchData = () => {
      stops
        .getTimesForStop(stop.id, 6)
        .then(data => setDepartures(data));
    };

    fetchData();

    const interval = setInterval(() => {
      console.log("Fetching new data");
      fetchData();
    }, 60 * 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex max-h-full flex-col p-2 text-xl border-2">
      <div className="mb-3 border-b-4">
        <h2>{stop.nazwa} </h2>
      </div>
      <span className="">
        {departures.map((departure) => (
          <DepartureComponent departure={departure} />
        ))}
      </span>
    </div>
  )
};
