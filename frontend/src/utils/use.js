import axios from "axios";
import VueSimpleAlert from "vue-simple-alert";

export function useVueSimpleAlert() {
  return VueSimpleAlert;
}

export const notify = VueSimpleAlert;

export function useAxios() {
  return axios;
}
