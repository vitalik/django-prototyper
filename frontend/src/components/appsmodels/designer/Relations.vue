<template>

    <svg :height="height" :width="width">
        <line v-for="(line, key) in all_relations" 
            :key="key" 
            :x1="line.from_left" 
            :y1="line.from_top" 
            :x2="line.to_left"
            :y2="line.to_top" 
            :class="line.class" />
    </svg>
</template>

<script>

export default {
    props: {
        models:   {type: Array, required: true},
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
            let pos = {}
            _.each(this.models, (m) => {
                pos[m.key] = {x: m.model.ui_left, y: m.model.ui_top, selected:m.selected}
            })

            let result = []
            _.each(this.models, (m) => {
                _.each(m.model.fields, (fld) => {
                    if (!fld.relation || !pos[m.key] || !pos[fld.relation])
                        return
                    
                    let cls = 'rel-muted'
                    if (m.selected)
                        cls = 'rel-to'
                    else if (pos[fld.relation].selected)
                        cls = 'rel-from'
                    
                    result.push({
                        from_top: pos[m.key].y,
                        from_left: pos[m.key].x,
                        to_top: pos[fld.relation].y,
                        to_left: pos[fld.relation].x,
                        class: cls,
                    })
                })
            })
            return result
        },
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
        stroke:  rgb(0, 0, 200);
        stroke-width: 1;
    }
</style>
