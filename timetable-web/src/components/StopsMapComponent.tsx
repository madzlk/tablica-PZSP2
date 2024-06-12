"use client";

import { useEffect, useState } from "react";
import { StopsMap } from "../types/StopsMap";
import { Location } from "../types/Location";
import { StopComponent } from "./StopComponent";
import { APIProvider, AdvancedMarker, Map } from "@vis.gl/react-google-maps";
import { FaSchool } from "react-icons/fa";

interface Props {
  mapStops: StopsMap;
  lastUpdated: string;
  location: Location;
}

export const StopsMapComponent = ({ mapStops, lastUpdated, location }: Props) => {
  const [time, setTime] = useState<Date>(new Date(Date.now()));

  useEffect(() => {
    var timer = setInterval(() => setTime(new Date()), 1000);

    return () => {
      clearInterval(timer);
    };
  }, []);

  console.log("Latitude", location.Latitude);
  console.log("Longitude", location.Longitude);

  return (
    <APIProvider apiKey={import.meta.env.VITE_MAPS_API_KEY}>
      <Map
        zoom={16.61}
        center={{ lat: 52.21858, lng: 21.013381991779095 }}
        mapId="805ef0f3bc515e9"
        mapTypeControl={false}
        zoomControl={false}
        streetViewControl={false}
        fullscreenControl={false}
      >
        <div className="absolute left-0 top-0 text-white z-10 m-3 py-1 px-3 text-2xl bg-[#B49FAA] shadow-md">
          {time.getHours() +
            ":" +
            time.getMinutes().toString().padStart(2, "0")}
        </div>
        <div className="absolute right-0 top-0 text-white text-sm z-10 m-3 py-1 px-3 bg-[#B49FAA] bg-opacity-50 shadow-md">
          Dane pobrane z api.um.warszawa.pl o: {lastUpdated.slice(0, -7)}
        </div>
        <AdvancedMarker position={{ lat: location.Latitude, lng: location.Longitude }}>
          <FaSchool size={36}  className=" text-[#303a94]"/>
        </AdvancedMarker>
        {mapStops.stops.map((stop, index) => (
          <StopComponent stop={stop} key={stop.id} componentId={index + 1} />
        ))}
      </Map>
    </APIProvider>
  );
};
