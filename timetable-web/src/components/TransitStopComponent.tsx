import { TransitStop } from "../types/TransitStop";
import { DepartureComponent } from "./DepartureComponent";
import { useEffect, useState } from "react";
import stops from "../services/stops";
import { Departure } from "../types/Departure";
import { BiWalk } from "react-icons/bi";

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
        <div className="flex flex-row justify-between">
          <h2>
            {stop.nazwa} {" " + stop.id.toString().slice(-2)}
          </h2>
          <div className="bg-[#7895CF] rounded-md px-1 text-xs lg:text-sm xl:text-base ml-1 font-semibold flex items-center">
            <BiWalk/> {stop.odleglosc} min
          </div>
        </div>
      </div>
      <div className="flex flex-col justify-around gap-1 h-full p-1 text-white">
        {departures.map((departure) => (
          <DepartureComponent departure={departure} />
        ))}
      </div>
    </div>
  );
};
