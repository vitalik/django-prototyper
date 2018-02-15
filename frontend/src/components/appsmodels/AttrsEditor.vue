<template>
    <div>
        <table>
            <Attr v-for="attr in field_attrs" :field="field" :attr="attr" :key="attr" />
        </table>
        
        <div style="font-size: 12px; background-color: #f5f5f5;">
            <pre>{{field}}</pre>
        </div>
    </div>
</template>

<script>

import {COMMON_ATTRIBUTES, FIELDS} from '../../django/fields'
import Attr from './Attr'
import {concat} from 'lodash'


export default {
    name: 'attrs-editor',
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
        Attr,
    }
}
</script>

