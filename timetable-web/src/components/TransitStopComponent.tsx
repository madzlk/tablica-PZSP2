import { TransitStop } from "../types/TransitStop";
import { DepartureComponent } from "./DepartureComponent";
import { useEffect, useState } from "react";
import stopsService from "../services/stops";
import { Departure } from "../types/Departure";
import { BiWalk } from "react-icons/bi";

interface Props {
  stop: TransitStop;
  stops: TransitStop[];
}

export const TransitStopComponent = ({ stop, stops }: Props) => {
  const [departures, setDepartures] = useState<Departure[]>([]);

  useEffect(() => {
    const fetchData = () => {
      stopsService.getTimesForStop(stop.id, 6).then((data) => setDepartures(data));
    };

    fetchData();

    const interval = setInterval(() => {
      console.log("Fetching new data");
      fetchData();
    }, 60 * 1000);

    return () => clearInterval(interval);
  }, [stops]);

  return (
    <div className="flex flex-col bg-[#B49FAA] text-nowrap leading-tight">
      <div className="mb-1 bg-white p-1 px-2 text-xl font-semibold">
        <div className="flex flex-row justify-between">
          <div className="flex items-center">
            <div className="bg-[#7895CF] rounded-md px-1 mr-1 py-[2px] text-xs lg:text-sm xl:text-base font-semibold text-white">
              {stop.nazwa[0].toUpperCase() + stop.id.toString().slice(-2)}
            </div>
            <h2 className="text-base">
              {stop.nazwa} {" " + stop.id.toString().slice(-2)}
            </h2>
          </div>
          <div className="rounded-md px-1 text-xs lg:text-sm xl:text-base ml-1 font-semibold flex items-center text-black">
            <BiWalk /> {stop.odleglosc} min
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
