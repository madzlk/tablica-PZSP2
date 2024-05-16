"use client";

import { StopsMap } from "../types/StopsMap";
import { StopComponent } from "./StopComponent";
import { APIProvider, Map } from "@vis.gl/react-google-maps";


interface Props {
  mapStops: StopsMap;
}

export const StopsMapComponent = ({ mapStops }: Props) => {
  // const [ lat, setLat ] = useState<number>(0);
  // const [ lng, setLng ] = useState<number>(0);

  // const defineCenter = (mapStops: TransitStop[]) => {
  //     let center = {lat: 0, lng: 0};
  //     for (let i = 0; i < mapStops.length; i++)
  //     {
  //         center.lat += mapStops[i].szer_geo;
  //         center.lng += mapStops[i].dlug_geo;
  //     }
  //     center.lat /= mapStops.length;
  //     center.lng /= mapStops.length;
  //     return center
  // };

  // useEffect(() => {
  //     const obj = defineCenter(mapStops.stops);
  //     setLat(obj.lat);
  //     setLng(obj.lng);
  // }, [mapStops])

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
        {mapStops.stops.map((stop, index) => (
          <StopComponent stop={stop} key={stop.id} componentId={index+1}/>
        ))}
      </Map>
    </APIProvider>
  );
};
