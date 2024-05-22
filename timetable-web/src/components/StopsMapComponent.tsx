"use client";

import { useEffect, useState } from "react";
import { StopsMap } from "../types/StopsMap";
import { StopComponent } from "./StopComponent";
import { APIProvider, Map } from "@vis.gl/react-google-maps";

interface Props {
  mapStops: StopsMap;
}

export const StopsMapComponent = ({ mapStops }: Props) => {
  const [time, setTime] = useState<Date>(new Date(Date.now()));

  useEffect(() => {
    var timer = setInterval(()=>setTime(new Date()), 1000)

    return () => {
      clearInterval(timer)
    };
  }, []);


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
        {mapStops.stops.map((stop, index) => (
          <StopComponent stop={stop} key={stop.id} componentId={index + 1} />
        ))}
      </Map>
    </APIProvider>
  );
};
