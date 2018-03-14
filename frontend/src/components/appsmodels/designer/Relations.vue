<template>
    <svg :height="height" :width="width">
        <line v-for="(line, key) in lines" 
            :key="key" 
            :x1="line.from_left" 
            :y1="line.from_top" 
            :x2="line.to_left"
            :y2="line.to_top" 
            class="foreignkey-line" />
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
        selected_model() {
            // outputs object if only one model is selected
            if (this.selected.length != 1)
                return null
            return _.find(this.models, {key:this.selected[0]}).model
        },
        rel_to_models() {
            if (this.selected_model === null)
                return []
            let rel_fields = _.filter(this.selected_model.fields, f => f.relation)
            return _.filter(this.models, (m) => {
                let ind = _.findIndex(rel_fields, (f) => f.relation == m.key)
                return ind != -1
            })
        },
        lines() {
            let m = this.selected_model
            return _.map(this.rel_to_models, (rel) => {
                console.info(rel)
                return {
                    from_top: rel.model.ui_top,
                    from_left: rel.model.ui_left,
                    to_top: m.ui_top,
                    to_left: m.ui_left,
                }
            })
        },
    }
}

</script>


<style scoped>
  .foreignkey-line {
    stroke: rgb(255, 0, 0);
    stroke-width: 2;
  }
</style>
