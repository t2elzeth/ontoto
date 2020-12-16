import { computed } from "vue";

export const defaultLayout = "default";

export function getLayout(route, key = "layout") {
  return computed(() => {
    return route.meta[key] || defaultLayout;
  });
}
