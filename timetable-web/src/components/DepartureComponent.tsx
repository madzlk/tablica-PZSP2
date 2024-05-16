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
    var difference = 0;
    if (arrival < now) {
      var midnight = new Date();
      midnight.setHours(24);
      midnight.setMinutes(0);
      midnight.setSeconds(0);
      midnight.setMilliseconds(0);

      var until_midnight = Math.floor(
        (midnight.getTime() - new Date().getTime()) / (1000 * 60)
      );

      var arrivalDate = parseArrivalTime(departure.czas_przyjazdu);

      difference =
        until_midnight + arrivalDate.getMinutes() + arrivalDate.getHours() * 60;
    } else {
      difference = Math.floor((arrival - now) / (1000 * 60));
    }

    if (difference === 0) {
      return "< 1";
    } else if (difference < 60) {
      return (
        <>
          {difference}
          <div className="text-xs xl:text-sm">min</div>
        </>
      );
    } else {
      const hours = Math.floor(difference / 60);
      const minutes = difference % 60;
      return (
        <>
          {hours}
          <div className="text-xs xl:text-sm">h</div>
          {minutes.toString().padStart(2, "0")}
          <div className="text-xs xl:text-sm">min</div>
        </>
      );
    }
  };

  const currentTime = new Date().getTime();
  const arrivalTime = parseArrivalTime(departure.czas_przyjazdu).getTime();

  return (
    <div className="flex flex-grow justify-between items-center  bg-[#3B3B4B] p-1 text-xs md:text-sm lg:text-base xl:text-xl">
      <div className="flex flex-row gap-2 items-center">
        <div className="bg-[#7895CF] rounded-md px-1 text-xs lg:text-sm xl:text-base ml-1 font-semibold">
          {departure.linia}
        </div>
        <div>{departure.kierunek}</div>
      </div>

      <div className="flex flex-row items-baseline">
        {displayArrivalTime(arrivalTime, currentTime)}
      </div>
    </div>
  );
};
