import { AdvancedMarker } from "@vis.gl/react-google-maps";
import { Stop } from "../types/Stop";

interface Props {
  stop: Stop;
  componentId: number;
}

export const StopComponent = ({ stop, componentId }: Props) => {
    return (
        <AdvancedMarker position={{lat: stop.szer_geo, lng: stop.dlug_geo}}>
            <div className="bg-[#7895CF] rounded-md px-1 text-base xl:text-sm font-semibold text-white">
                {stop.nazwa[0].toUpperCase() + stop.id.toString().slice(-2)}
            </div>
        </AdvancedMarker>
    );
};
