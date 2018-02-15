<template>

    <select v-model="selection" @change="$emit('input', selection)" style="width: auto;">
        <option :value="null" v-if="canbenull">None</option>
        <option :value="true">True</option>
        <option :value="false">False</option>
    </select>

</template>

<script>

export default {
    name: 'InputTrueFalse',
    props: {
        value: {required: true},
        canbenull: {required: false, type: Boolean, default: false}
    },
    data() {
        return {
            selection: false,
        }
    },
    mounted() {
        this.selection = this.value
    },
    watch: {
        value(new_val) {
            this.selection = new_val
        }
    }
}
</script>
