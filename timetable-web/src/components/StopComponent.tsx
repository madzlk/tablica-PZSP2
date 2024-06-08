import { AdvancedMarker } from "@vis.gl/react-google-maps";
import { TransitStop } from "../types/TransitStop";

interface Props {
  stop: TransitStop;
  componentId: number;
}

export const StopComponent = ({ stop, componentId }: Props) => {
    return (
        <AdvancedMarker key={componentId} position={{lat: stop.szer_geo, lng: stop.dlug_geo}}>
            <div className="bg-[#7895CF] rounded-md px-1 text-base xl:text-sm font-semibold text-white">
                {stop.nazwa[0].toUpperCase() + stop.id.toString().slice(-2)}
            </div>
        </AdvancedMarker>
    );
};
