<template>

    <svg :height="height" :width="width">
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

    export default {
        props: {
            models: {type: Array, required: true},
            selected: {type: Array, required: true},
        },
        data() {
            return {
                height: window.innerHeight,
                width: window.innerWidth,
            }
        },
        computed: {
            all_relations() {
                function closest_dots(first_block, second_block) {
                    function distance(x1, y1, x2, y2) {
                        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))
                    }

                    // all edges of the blocks
                    const f1 = {x: first_block.x1, y: first_block.y1, middle: false};
                    const f2 = {x: first_block.x2, y: first_block.y1, middle: false};
                    const f12 = {x: (f1.x + f2.x) / 2, y: (f1.y + f2.y) / 2, middle: true};
                    const f3 = {x: first_block.x2, y: first_block.y2, middle: false};
                    const f23 = {x: (f2.x + f3.x) / 2, y: (f2.y + f3.y) / 2, middle: true};
                    const f4 = {x: first_block.x1, y: first_block.y2, middle: false};
                    const f34 = {x: (f3.x + f4.x) / 2, y: (f3.y + f4.y) / 2, middle: true};
                    const f41 = {x: (f4.x + f1.x) / 2, y: (f4.y + f1.y) / 2, middle: true};

                    const s1 = {x: second_block.x1, y: second_block.y1, middle: false};
                    const s2 = {x: second_block.x2, y: second_block.y1, middle: false};
                    const s12 = {x: (s1.x + s2.x) / 2, y: (s1.y + s2.y) / 2, middle: true};
                    const s3 = {x: second_block.x2, y: second_block.y2, middle: false};
                    const s23 = {x: (s2.x + s3.x) / 2, y: (s2.y + s3.y) / 2, middle: true};
                    const s4 = {x: second_block.x1, y: second_block.y2, middle: false};
                    const s34 = {x: (s3.x + s4.x) / 2, y: (s3.y + s4.y) / 2, middle: true};
                    const s41 = {x: (s4.x + s1.x) / 2, y: (s4.y + s1.y) / 2, middle: true};

                    const firsts = [f1, f2, f3, f4, f12, f23, f34, f41];
                    const seconds = [s1, s2, s3, s4, s12, s23, s34, s41];
                    let results = [0, 0, 0, 0];
                    let min = Number.MAX_SAFE_INTEGER;
                    // find the closet dots
                    for (let i = 0; i < firsts.length; i++) {
                        for (let k = 0; k < firsts.length; k++) {
                            const x1 = firsts[i].x;
                            const y1 = firsts[i].y;
                            const middle1 = firsts[i].middle;
                            const x2 = seconds[k].x;
                            const y2 = seconds[k].y;
                            const middle2 = seconds[k].middle;

                            const dist = distance(x1, y1, x2, y2);
                            // five priority to center coordinates
                            if (dist < min ||
                                (dist - 20 < min && (middle1 || middle2))
                                || (dist - 30 < min && middle1 && middle2)) {
                                let priority;
                                if (dist - 30 < min){
                                    priority = 28;
                                }
                                else if (dist - 20 < min){
                                    priority = 18;
                                }
                                min = dist - priority;
                                results = [x1, y1, x2, y2]
                            }
                        }
                    }
                    return results;
                }

                let pos = {}
                _.each(this.models, (m) => {
                    pos[m.key] = {
                        //approximate coordinates of edges
                        x1: m.model.ui_left - 20,
                        y1: m.model.ui_top - 20,
                        x2: m.model.ui_left + 130,
                        y2: m.model.ui_top + (m.model.fields.length * 23),
                        selected: m.selected
                    }
                })

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
                        let x1, y1, x2, y2;
                        [x1, y1, x2, y2] = closest_dots(pos[m.key], pos[fld.relation]);
                        console.log(x1, y1, x2, y2);
                        result.push({
                            from_left: x1,
                            from_top: y1,
                            to_left: x2,
                            to_top: y2,
                            class: cls,
                        })
                    })
                })
                return result
            },
        },
        methods: {
            get_triangle(line) {
                if (line.class === 'rel-muted' || (line.class !== 'rel-to' && line.class !== 'rel-from')) return;
                const x1 = line.from_left;
                const y1 = line.from_top;
                const x2 = line.to_left;
                const y2 = line.to_top;
                console.log(x1, y1);
                console.log(x2, y2);
                const middle_x = (x1 + x2) / 2;
                const middle_y = (y1 + y2) / 2;

                // find the proportions if which line from center to the top of triangle divides the half of the line
                const top_lamb = (10) / ((Math.sqrt(Math.pow(x2 - middle_x, 2) + Math.pow(y2 - middle_y, 2))) - 10);
                // find top coords by formula
                let x_top = (middle_x + top_lamb * x2) / (1 + top_lamb);
                let y_top = (middle_y + top_lamb * y2) / (1 + top_lamb);

                //params of line equation
                let B_main = (x2 - x1);
                const A_main = (y1 - y2);
                const C_main = (x1 * y2 - x2 * y1);


                // params of line equation that is parallel to the main
                const C_left = C_main + 10 * (Math.sqrt(A_main * A_main + B_main * B_main));
                const C_right = C_main - 10 * (Math.sqrt(A_main * A_main + B_main * B_main));
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
