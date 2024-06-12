import axios from "axios";
import { Stop } from "../types/Stop";
import { Location } from "../types/Location";

const baseUrl = "/api";

const getAllStops = (): Promise<Stop[]> => {
  const request = axios.get(`${baseUrl}/stops`);
  return request.then((response) => response.data);
};

const getTimesForStop = (stopId: number, numberOfStops: number) => {
  const request = axios.get(`${baseUrl}/times/${stopId}/${numberOfStops}`);
  return request.then((response) => response.data);
};

const getLocation = () : Promise<Location> => {
  const request = axios.get(`${baseUrl}/project_location`);
  return request.then((response) => response.data);
};

const adjustDistances = (data: Stop[]): Stop[] => {
  const shift = 0.00002;
  const long_shift = 0.0002;
  for (let i = 0; i < data.length; i++) {
    for (let j = i + 1; j < data.length; j++) {
      const distance = Math.sqrt(
        Math.abs(data[i].dlug_geo - data[j].dlug_geo) ** 2 +
          Math.abs(data[i].szer_geo - data[j].szer_geo)
      );

      if (distance < 0.01) {
        if (data[i].dlug_geo > data[j].dlug_geo) {
          data[i].dlug_geo += long_shift;
          data[j].dlug_geo -= long_shift;
        } else {
          data[i].dlug_geo -= long_shift;
          data[j].dlug_geo += long_shift;
        }
        if (data[i].szer_geo > data[j].szer_geo) {
          data[i].szer_geo += shift;
          data[j].szer_geo -= shift;
        } else {
          data[i].szer_geo -= shift;
          data[j].szer_geo += shift;
        }
      }
    }
  }
  return data;
};

export default { getAllStops, getTimesForStop, getLocation, adjustDistances };
