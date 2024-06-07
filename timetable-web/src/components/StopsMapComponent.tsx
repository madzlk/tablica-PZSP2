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
  const [bounds, setBounds] = useState<google.maps.LatLngBoundsLiteral | undefined>(undefined);

  useEffect(() => {
    const timer = setInterval(() => setTime(new Date()), 1000);

    return () => {
      clearInterval(timer);
    };
  }, []);

  useEffect(() => {
    if (mapStops.stops.length > 0) {
      let minLat = mapStops.stops[0].szer_geo;
      let maxLat = mapStops.stops[0].szer_geo;
      let minLng = mapStops.stops[0].dlug_geo;
      let maxLng = mapStops.stops[0].dlug_geo;

      mapStops.stops.forEach((stop) => {
        if (stop.szer_geo < minLat) minLat = stop.szer_geo;
        if (stop.szer_geo > maxLat) maxLat = stop.szer_geo;
        if (stop.dlug_geo < minLng) minLng = stop.dlug_geo;
        if (stop.dlug_geo > maxLng) maxLng = stop.dlug_geo;
      });


      console.log("minLat", minLat);
      console.log("maxLat", maxLat);
      console.log("minLng", minLng);
      console.log("maxLng", maxLng);

      setBounds({
        north: maxLat,
        south: minLat,
        east: maxLng,
        west: minLng,
      });
    }
  }, [mapStops]);

  return (
    <APIProvider apiKey={import.meta.env.VITE_MAPS_API_KEY}>
      <Map
        defaultBounds={bounds}
        mapId="805ef0f3bc515e9"
        mapTypeControl={false}
        zoomControl={false}
        streetViewControl={false}
        fullscreenControl={false}
      >
        <div className="absolute left-0 top-0 text-white z-10 m-3 py-1 px-3 text-2xl bg-[#B49FAA] shadow-md">
          {time.getHours() + ":" + time.getMinutes().toString().padStart(2, "0")}
        </div>
        {mapStops.stops.map((stop, index) => (
          <StopComponent stop={stop} key={stop.id} componentId={index + 1} />
        ))}
      </Map>
    </APIProvider>
  );
};
