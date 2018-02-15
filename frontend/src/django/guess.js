import { startsWith, endsWith, includes } from 'lodash'


export function guess_type(name) {
    if (startsWith(name, 'is_') || startsWith(name, 'has_') || startsWith(name, 'have_') || startsWith('allow_') || startsWith('can_'))
        return 'BooleanField'
    
    if (includes(name, 'slug'))
        return 'SlugField'
    
    if (includes(name, 'time'))
        return 'DateTimeField'
    
    if (includes(name, 'date'))
        return 'DateField'
    
    if (includes(name, 'duration'))
        return 'DurationField'
    
    if (includes(name, 'email'))
        return 'EmailField'
    
    if (endsWith(name, 'url'))
        return 'URLField'
    
    if (includes(name, 'file') || includes(name, 'pdf'))
        return 'FileField'
    
    if (includes(name, 'image') || includes(name, 'picture') || includes(name, 'photo') || includes(name, 'avatar'))
        return 'ImageField'
    
    if (includes(name, 'text') || includes(name, 'description') || includes(name, 'message') || includes(name, 'intro') || includes(name, 'content'))
        return 'TextField'
    
    return 'CharField'
}
