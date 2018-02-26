<template>
    <div class="text-nowrap">
        <select v-model="field.type" @focus="$emit('focus')">
            <option v-for="t in type_choices">{{t}}</option>
        </select>
        <select v-if="is_relational_type" v-model="field.relation">
            <option :value="null">Select model...</option>
            <option v-for="model in relation_options">{{model}}</option>
        </select>

    </div>
</template>

<script>
import _ from 'lodash'
import { store } from '../../store'
import { FIELDS, RELATIONAL_FIELDS } from '../../django/fields'

export default {
    name: 'field-type',
    props: {
        field: {
            required: true,
            type: Object
        }
    },
    computed: {
        type_choices() {
            return _.keys(FIELDS)
        },
        is_relational_type() {
            return _.indexOf(RELATIONAL_FIELDS, this.field.type) >= 0
        },
        relation_options() {
            return store.models_keys()
        }
    },
    methods: {
        on_type_change(val, arg2) {
            alert([val, arg2])
        }
    }
}
</script>

