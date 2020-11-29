import { notify } from "@/utils/pluginsConstants";

export function alert(title, message, type = "info") {
  return notify.alert(message, title, type);
}

export function error(message, title = "Error!") {
  return notify.alert(message, title, "error");
}

export function success(message, title = "Success!") {
  return notify.alert(message, title, "success");
}
