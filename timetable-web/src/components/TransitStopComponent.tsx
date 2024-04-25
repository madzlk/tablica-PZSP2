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
      stops.getTimesForStop(stop.id, 6).then((data) => setDepartures(data));
    };

    fetchData();

    const interval = setInterval(() => {
      console.log("Fetching new data");
      fetchData();
    }, 60 * 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex flex-col bg-[#B49FAA] text-nowrap leading-tight">
      <div className="mb-1 bg-white p-1 px-2 text-xl font-semibold">
        <h2>{stop.nazwa} </h2>
      </div>
      <div className="flex flex-col justify-around gap-1 h-full p-1 text-white">
        {departures.map((departure) => (
          <DepartureComponent departure={departure} />
        ))}
      </div>
    </div>
  );
};
