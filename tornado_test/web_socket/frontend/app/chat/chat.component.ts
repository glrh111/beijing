

interface banner {
    action_cn: string;
    title: string;
    url: string;
    image: string;
    create_at: number;
}

class Banner implements banner {
    constructor (
        public action_cn: string,
        public title: string,
        public url: string,
        public image: string,
        public create_at: number
    ) { }
}

export class BannerComponent {
    public get_banners() {
        JQuery.
    }
}