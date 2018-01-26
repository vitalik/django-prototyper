<template>
    <div class="input-group" :class="{'input-group-sm': small}">
        <input @input="validate($event.target.value)"
           @keyup.enter="save"
           v-model="val"
           :placeholder="placeholder"
           :class="{'text-danger': !is_valid}"
           class="form-control">
        <div class="input-group-append">
            <button @click="save"
                class="btn" 
                :class="{disabled:!is_valid, 'btn-primary':is_valid, 'btn-outline-secondary':!is_valid}">
                    {{btnlabel}}
            </button>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">
export default {
    name: 'pattern-input',
    props: {
        default: {
            default: '',
            type: [Number, String]
        },
        regExp: {
            type: RegExp,
            default: null
        },
        small: {
            default: false,
            type: Boolean,
        },
        btnlabel: {default: "Save"},
        placeholder: {type: String}
    },
    data() {
        return {
            val: '',
            is_valid: false,
        };
    },
    mounted() {
        this.val = this.default;
        this.validate(this.val)
    },
    methods: {
        validate(val) {
            this.is_valid = val.toString().match(this.regExp) != null;
        },

        save() {
            if (!this.is_valid)
                return
            let res = this.$emit('save', this.val)
            this.val = ''
            this.is_valid = false
        },

    }
}
</script>
