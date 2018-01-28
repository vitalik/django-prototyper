<template>

    <select v-model.boolean="selection" @change="$emit('input', selection)" style="width: auto;">
        <option :value="true">True</option>
        <option :value="false">False</option>
    </select>

</template>

<script>

export default {
    name: 'InputTrueFalse',
    props: ['value'],
    data() {
        return {
            selection: false,
        }
    },
    mounted() {
        this.selection = this.value
    }
}
</script>
