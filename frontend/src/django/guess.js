import { startsWith, endsWith, includes } from 'lodash'


export function guess_type(name) {
    if (startsWith(name, 'is_') || startsWith(name, 'has_') || startsWith(name, 'have_') || startsWith('allow_'))
        return 'models.BooleanField'
    
    if (includes(name, 'slug'))
        return 'models.SlugField'
    
    if (includes(name, 'time'))
        return 'models.DateTimeField'
    
    if (includes(name, 'date'))
        return 'models.DateField'
    
    if (includes(name, 'duration'))
        return 'models.DurationField'
    
    if (includes(name, 'email'))
        return 'models.EmailField'
    
    if (endsWith(name, 'url'))
        return 'models.UrlField'
    
    if (includes(name, 'file') || includes(name, 'pdf'))
        return 'models.FileField'
    
    if (includes(name, 'image') || includes(name, 'picture') || includes(name, 'photo') || includes(name, 'avatar'))
        return 'models.ImageField'
    
    if (includes(name, 'text') || includes(name, 'description') || includes(name, 'message') || includes(name, 'intro') || includes(name, 'content'))
        return 'models.TextField'
    
    return 'models.CharField'
}
