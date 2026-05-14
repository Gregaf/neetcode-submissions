
class ItemNode<T, E> {
    public next: ItemNode<T, E> | undefined;
    public prev: ItemNode<T, E> | undefined;
    constructor(public key: T, public val: E) {}
}

class LRUCache {
    // Backing store will be map/dict
    private readonly cacheMap: Map<number, ItemNode<number, number>>;
    private capacity: number;

    private left: ItemNode<number, number>;
    private right: ItemNode<number, number>;

    /**
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.capacity = capacity;
        this.cacheMap = new Map<number, ItemNode<number, number>>();
        this.left = new ItemNode(0, 0);
        this.right = new ItemNode(0, 0);
        
        this.left.next = this.right;
        this.right.prev = this.left;
    }

    private remove(node: ItemNode<number, number>) {
        const prev = node.prev;
        const next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    private insert(node: ItemNode<number, number>) {
        const prev = this.right.prev;
        prev.next = node;
        node.prev = prev;
        node.next = this.right;
        this.right.prev = node;
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {
        const node = this.cacheMap.get(key);
        if (node === undefined) {
            return -1;
        }
        this.remove(node);
        this.insert(node);

        return node.val;
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {
        if (this.cacheMap.has(key)) {
            this.remove(this.cacheMap.get(key));
        }
        const newNode = new ItemNode(key, value);
        this.cacheMap.set(key, newNode);
        this.insert(newNode);

        if (this.cacheMap.size > this.capacity) {
            const lruNode = this.left.next;
            this.remove(lruNode);
            this.cacheMap.delete(lruNode.key);
        }
    }
}
