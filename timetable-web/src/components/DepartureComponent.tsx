import { Departure } from "../types/Departure";

interface Props {
  departure: Departure;
}

export const DepartureComponent = ({ departure }: Props) => {
  return (
    <div className="flex flex-row justify-between">
      <div>
        {departure.line} - {departure.direction}
      </div>
      <div>{departure.arrivalTime.toTimeString().slice(0, 5)}</div>
    </div>
  );
};
