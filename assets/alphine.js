// import './styles/app.css'
import { startStimulusApp } from '@symfony/stimulus-bridge';

export const alphine = startStimulusApp(require.context(
    '@symfony/stimulus-bridge/lazy-controller-loader!./controllers',
    true,
    /\.[jt]sx?$/
));