<template>
    <div>
        <table style="width: 100%;">
            <field-attr v-for="attr in field_attrs" :field="field" :attr="attr" :key="attr" />
        </table>
    </div>
</template>

<script>

import {COMMON_ATTRIBUTES, FIELDS} from '../../django/fields'
import FieldAttr from './FieldAttr'
import {concat} from 'lodash'


export default {
    name: 'field-attrs-editor',
    props: {
        field: {
            required: true,
            type: Object
        }
    },
    computed: {
        field_attrs() {
            let field_attrs = FIELDS[this.field.type]
            return concat(field_attrs, COMMON_ATTRIBUTES)
        }
    },
    components: {
        FieldAttr,
    }
}
</script>

