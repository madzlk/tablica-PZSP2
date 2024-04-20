"use client";

import { useEffect, useState } from "react";
import { StopsMap } from "../types/StopsMap";
import { StopComponent } from "./StopComponent";
import { Stop } from "../types/Stop";
import {
    APIProvider,
    Map,
} from "@vis.gl/react-google-maps";

interface Props {
  mapSettings: StopsMap;
}

export const StopsMapComponent = ({ mapSettings }: Props) => {
    const [ stops, setStops ] = useState<Stop[]>([]);

    const mockedStops: Stop[] = [{
        lat: 52.21765094183412,
        lng: 21.014004264559684,
        stopName: "Metro Politechnika",
        stopType: "metro",
        id: 1
    },
    {
        lat: 52.21992379181962,
        lng: 21.01151517475397,
        stopName: "Plac Politechniki",
        stopType: "tram",
        id: 2
    },
    {
        lat: 52.2191035880524,
        lng: 21.015699420494222,
        stopName: "Metro Politechnika",
        stopType: "bus",
        id: 3
    }]

    useEffect(() => {
        setStops(mockedStops);
    }, [])

    return (
        <APIProvider apiKey="AIzaSyClFmc-czRNbD52FAMn1ZZtwsKUHCXTQm0">
            <Map zoom={mapSettings.zoom} center={{lat: mapSettings.centerLat, lng: mapSettings.centerLng}} mapId="805ef0f3bc515e9" mapTypeControl={false} zoomControl={false} streetViewControl={false} fullscreenControl={false}>
                {stops.map(stop => <StopComponent stop={stop}/>)}
            </Map>
        </APIProvider>
    );
};
