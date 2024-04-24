import { AdvancedMarker } from "@vis.gl/react-google-maps";
import { Stop } from "../types/Stop";

interface Props {
  stop: Stop;
}

export const StopComponent = ({ stop }: Props) => {
    return (
        <AdvancedMarker position={{lat: stop.szer_geo, lng: stop.dlug_geo}}>
            <div style={{height: '30px', width: '60px'}}>
                <p style={{color: 'blue'}}><b>{stop.nazwa}</b></p>
            </div>
        </AdvancedMarker>
    );
};
