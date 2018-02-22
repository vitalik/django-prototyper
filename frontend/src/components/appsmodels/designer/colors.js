import { random } from 'lodash'
import { store } from '../../../store'

export const APP_COLORS = [
    "#F77A5E",
    "#D7E684",
    "#FFF7C1",
    "#1FD8A8",
    "#9CC4E4",
    "#B7E6F2",
    "#C1ABB7",
    "#DAC9B7",
    "#eeeeee",
    "#9AAF90",
]


export function get_some_color() {
    return APP_COLORS[_.random(APP_COLORS.length-1)]
}