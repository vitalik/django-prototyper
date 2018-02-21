<template>
    <span :class="{'badge-secondary': value == initial, 'badge-primary': value != initial}" class="badge" @click="toggle" style="cursor: pointer;">
        <span :style="{opacity: this.value ? 1 : 0}">V</span>
        {{ label }}
    </span>
</template>

<script>

export default {
    name: 'CheckLabel',
    props: {
        value: {required: true, type: Boolean},
        initial: {required: true, type: Boolean},
        label: {required: true, type: String},
    },
    methods: {
        toggle() {
            this.$emit('input', !this.value)
        }
    },
    // data() {
    //     return {
    //         lable: false,
    //     }
    // },
    // mounted() {
    //     this.selection = this.value
    // },

}
</script>
