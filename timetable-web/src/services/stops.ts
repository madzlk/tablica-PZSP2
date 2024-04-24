import axios from 'axios';

const baseUrl = 'http://localhost:8000'

const getAllStops = () => {
    const request = axios.get(`${baseUrl}/stops`);
    return request.then(response => response.data);
}

const getTimesForStop = (stopId: number, numberOfStops: number) => {
    const request = axios.get(`${baseUrl}/times/${stopId}/${numberOfStops}`);
    return request.then(response => response.data);
}

export default { getAllStops, getTimesForStop };