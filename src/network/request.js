import axios from "axios";

export function get_goods(params){
    return axios('http://localhost:8000/goods/get_goods?'+params);
}