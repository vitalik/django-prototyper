<template>

    <svg>
        <template v-for="(line, key) in all_relations">
            <line :key="key"
                  :x1="line.from_left"
                  :y1="line.from_top"
                  :x2="line.to_left"
                  :y2="line.to_top"
                  :class="line.class">

            </line>
            <polygon :points="get_triangle(line)" style="fill:red;stroke:red;stroke-width:1"/>
        </template>
    </svg>
</template>

<script>
    import _ from 'lodash'

    export default {
        props: {
            models: {type: Array, required: true},
            selected: {type: Array, required: true},
        },
        computed: {
            all_relations() {
                let pos = {}
                _.each(this.models, (m) => {
                    pos[m.key] = {
                        x1: m.model.ui_left + 20,
                        y1: m.model.ui_top + 10,
                        selected: m.selected
                    }
                });

                let result = []
                _.each(this.models, (m) => {
                    _.each(m.model.fields, (fld) => {
                        if (!fld.relation || !pos[m.key] || !pos[fld.relation])
                            return;

                        let cls = 'rel-muted';
                        if (m.selected)
                            cls = 'rel-to';
                        else if (pos[fld.relation].selected)
                            cls = 'rel-from';
                        result.push({
                            from_left: pos[m.key].x1,
                            from_top: pos[m.key].y1,
                            to_left: pos[fld.relation].x1,
                            to_top: pos[fld.relation].y1,
                            class: cls,
                        })
                    })
                })
                return result
            }
        },
        methods: {
            get_triangle(line) {
                if (line.class === 'rel-muted' || (line.class !== 'rel-to' && line.class !== 'rel-from')) return;
                const x1 = line.from_left;
                const y1 = line.from_top;
                const x2 = line.to_left;
                const y2 = line.to_top;
                let middle_x = (x1 + x2) / 2;
                let middle_y = (y1 + y2) / 2;

                // make an in the right direction to make arrow visible
                if (y2 + 80 > y1 && x2 + 80 > x1) {
                    middle_x += (x2 - x1) * 0.15;
                    middle_y += (y2 - y1) * 0.15;
                }
                else if (y2 - 80 < y1 && x2 - 80 < x1) {
                    middle_x -= (x2 - x1) * 0.15;
                    middle_y -= (y2 - y1) * 0.15;
                }

                // find the proportions if which line from center to the top of triangle divides the half of the line
                const triangle_height = 20;
                const top_lamb = (triangle_height) / ((Math.sqrt(Math.pow(x2 - middle_x, 2) + Math.pow(y2 - middle_y, 2))) - triangle_height);
                // find top coords by formula
                let x_top = (middle_x + top_lamb * x2) / (1 + top_lamb);
                let y_top = (middle_y + top_lamb * y2) / (1 + top_lamb);

                //params of line equation
                let B_main = (x2 - x1);
                const A_main = (y1 - y2);
                const C_main = (x1 * y2 - x2 * y1);


                // params of line equation that is parallel to the main
                const triangle_half_width = 5;
                const C_left = C_main + triangle_half_width * (Math.sqrt(A_main * A_main + B_main * B_main));
                const C_right = C_main - triangle_half_width * (Math.sqrt(A_main * A_main + B_main * B_main));
                // params of line equation of the perpendicular line
                const A_perp = -B_main;
                const B_perp = A_main;
                const C_perp = A_main * (-middle_y) + B_main * (middle_x);

                //Kramer formula to solve equation system
                let x_left = -(C_left * B_perp - C_perp * B_main) / (A_main * B_perp - A_perp * B_main);
                let y_left = -(A_main * C_perp - A_perp * C_left) / (A_main * B_perp - A_perp * B_main);
                let x_right = -(C_right * B_perp - C_perp * B_main) / (A_main * B_perp - A_perp * B_main);
                let y_right = -(A_main * C_perp - A_perp * C_right) / (A_main * B_perp - A_perp * B_main);


                return `${x_top},${y_top} ${x_left},${y_left} ${x_right},${y_right}`
            }
        }
    }

</script>


<style scoped>
    .rel-muted {
        stroke-width: 1;
        stroke: rgba(0, 0, 0, 0.08);
    }

    .rel-to {
        stroke: rgb(0, 255, 0);
        stroke-width: 2;
    }

    .rel-from {
        stroke: rgb(0, 0, 200);
        stroke-width: 1;
    }
</style>
