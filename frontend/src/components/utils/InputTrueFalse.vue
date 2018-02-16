<template>

    <select v-model="selection" @change="$emit('input', selection)" style="width: auto;">
        <option :value="null" v-if="canbenull">None</option>
        <option :value="true">{{ true_label }}</option>
        <option :value="false">{{ false_label }}</option>
    </select>

</template>

<script>

export default {
    name: 'InputTrueFalse',
    props: {
        value: {required: true},
        canbenull: {required: false, type: Boolean, default: false},
        showdefault: {required: false, default: null}
    },
    data() {
        return {
            selection: false,
        }
    },
    mounted() {
        this.selection = this.value
    },
    computed: {
        true_label() {
            let suffix = ''
            if (this.showdefault === true)
                suffix = ' (default)'
            return 'True' + suffix
        },
        false_label() {
            let suffix = ''
            if (this.showdefault === false)
                suffix = ' (default)'
            return 'False' + suffix
        }
    },
    watch: {
        value(new_val) {
            this.selection = new_val
        }
    }
}
</script>
