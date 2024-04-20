import { AdvancedMarker } from "@vis.gl/react-google-maps";
import { Stop } from "../types/Stop";

interface Props {
  stop: Stop;
}

export const StopComponent = ({ stop }: Props) => {
    return (
        <AdvancedMarker position={{lat: stop.lat, lng: stop.lng}} key={stop.id}>
            <div style={{height: '30px', width: '60px'}}>
                <p style={{color: 'blue'}}><b>{stop.stopName}</b></p>
            </div>
        </AdvancedMarker>
    );
};
