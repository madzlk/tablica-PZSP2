import { TransitStop } from "../types/TransitStop";
import { DepartureComponent } from "./DepartureComponent";

interface Props {
  stop: TransitStop;
}

export const TransitStopComponent = ({ stop }: Props) => {
  return <div className="flex max-h-full flex-col p-2 text-xl border-2">
  <div className="mb-3 border-b-4">
    <h2>{stop.name} </h2>
  </div>
  <span className="">
    {stop.departures.map((departure) => (
      <DepartureComponent departure={departure} />
    ))}
  </span>
</div>
};
