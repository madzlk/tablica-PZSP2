import { Departure } from "./Departure";

// Bus or tram stop
export interface TransitStop {
  departures: Departure[]; // List of upcoming departures
  name: string; // e.g. Metro Politechnika 05
  walkTime: number; // Time it takes to walk to a given stop (in minutes)
  isBusStop: boolean;
  // TODO: and coordinates and number/id (to show on map)
}
