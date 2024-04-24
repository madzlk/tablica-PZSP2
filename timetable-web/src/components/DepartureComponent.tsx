import { Departure } from "../types/Departure";

interface Props {
  departure: Departure;
}

export const DepartureComponent = ({ departure }: Props) => {
  let parseArrivalTime = (timeString: string) => {
    let timeArray = timeString.split(":");
  
    let date = new Date();
    date.setHours(parseInt(timeArray[0]));
    date.setMinutes(parseInt(timeArray[1]));
    date.setSeconds(parseInt(timeArray[2]));

    return date;
  };

  let displayArrivalTime = (arrival: number, now: number) => {
    const difference = Math.floor((arrival - now) / (1000 * 60));
    if (difference === 0)
    {
      return "< 1";
    }
    return difference;
  };

  const currentTime = new Date().getTime();
  const arrivalTime = parseArrivalTime(departure.czas_przyjazdu).getTime();

  return (
    <div className="flex flex-row justify-between">
      <div>
        {departure.linia} - {departure.kierunek}
      </div>
      <div>{displayArrivalTime(arrivalTime, currentTime)}</div>
    </div>
  );
};
